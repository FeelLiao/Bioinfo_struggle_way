#!/usr/bin/bash

# global variable
raw_read_file=$1
pilon_dir=$HOME
prinseq_dir=$HOME/prinseq-lite-0.20.4
workdir=$(pwd)
# help info
echo "#####################################################################"
echo "#                                                                   #"
echo "# This script is used for genome assembly using minimap and miniasm #"
echo "#                                                                   #"
echo "#####################################################################"
echo "Usage: $0 <fq1>"
echo "fq1: the long read file"

echo ""

# function
check_conda () {
echo $PATH | grep conda >/dev/null 2>&1
if [[ $?=1 ]]; then
    echo "conda have been installed"
else
    echo "conda is not found on this computer"
    echo "Install miniconda from tsinghua mirror"
    cd $HOME
    wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh 
    bash ./Miniconda3-latest-Linux-x86_64.sh
fi
}

conda_tools () {
conda create --name minitools minimap2==2.17 miniasm=0.3_r179 racon==1.4.20  any2fasta -c bioconda -y
conda create --name gene_tools bwa==0.7.17 samtools==1.14 -c bioconda -y
conda create --name software_dependence perl openjdk -y
}

others_tools () {
prinseq_download_adress=https://sourceforge.net/projects/prinseq/files/standalone/prinseq-lite-0.20.4.tar.gz/download
pilon_download_adress=https://github.com/broadinstitute/pilon/releases/download/v1.24/pilon-1.24.jar
cd $HOME
wget -O prinseq-lite.tar.gz $prinseq_download_adress
wget -O pilon.jar $pilon_download_adress
tar -xzf ./prinseq-lite.tar.gz
}

genome_assembly () {
minimap2 -x ava-ont -L -m0 -t47 $raw_read_file $raw_read_file > ont.paf
miniasm -f $raw_read_file ont.paf > ONTmin.gfa
any2fasta ONTmin.gfa  > ONTmin_IT0.fasta
}

long_read_polishing () {
minimap2 ONTmin_IT0.fasta $raw_read_file > ONTmin_IT0.paf 
racon -t 47 $raw_read_file ONTmin_IT0.paf ONTmin_IT0.fasta > ONTmin_IT1.fasta
minimap2 ONTmin_IT1.fasta $raw_read_file > ONTmin_IT1.paf
racon -t 47 ont.fq ONTmin_IT1.paf ONTmin_IT1.fasta > ONTmin_IT2.fasta
minimap2 ONTmin_IT2.fasta $raw_read_file > ONTmin_IT2.paf
racon -t 47 $raw_read_file ONTmin_IT2.paf ONTmin_IT2.fasta > ONTmin_IT3.fasta
}

short_read_trim () {
perl $prinseq_dir/prinseq-lite.pl -fastq il_1.fq -fastq2 il_2.fq -min_len 100 -trim_qual_right 38 -min_qual_mean 38 -out_good il_trimmed
}
short_read_polishing () {
bwa index ONTmin_IT3.fasta
bwa mem -t 47 ONTmin_IT3.fasta il_trimmed_1.fastq il_trimmed_2.fastq | samtools view -@ 47 -bhS | samtools sort -@ 47 > ONTmin_IT3.bam
samtools index  ONTmin_IT3.bam
conda activate software_dependence
java -Xmx48G -jar $pilon_dir/pilon.jar --genome ONTmin_IT3.fasta --frags ONTmin_IT3.bam --fix snps --output ONTmin_IT4
}

# the main script
echo "your workdir is:"
echo "$workdir"
echo "your workdir should be the directory where you store the raw reads."
echo "now cheking if the conda environment"
check_conda
echo "the environmnet is ready, do you want to continue? y/n "
read -p "Please input your choice:" continue_choice
if [ "$continue_choice" == "y" ];then
    echo "now continue!"
    echo "---------------------------------------------------------"
    echo ""
    echo "install necessary software"
    conda_tools
    others_tools
    echo "software has installed!"
    echo "start genome assembly!"
    cd $workdir
    conda activate minitools
    genome_assembly
    long_read_polishing
    conda activate software_dependence
    short_read_trim
    conda activate gene_tools
    short_read_polishing
    echo "-----------------------------------------------------------"
    echo "all work done!"
else
    echo "exit!"
    exit 0;
fi

