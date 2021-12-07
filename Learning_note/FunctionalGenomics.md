# Functional Genomics 

`Common technologies and data analysis methods`

## 1. Real-time PCR

Real-time PCR is more sensitive than microarrays in detecting small changes in expression but requires more input RNA and is less adaptable to high-throughput studies. It is best suited for studies of small subsets of genes. The sequence of the target gene of interest must be known(To design the PCR primers) in this method. hence real-time PCR can only be used for studying known genes.

SYBR green and Taqman probes are two types of fluorescent reporters which are commonly used in real-time PCR. 

## 2. Microarrays

The probes that Microarrays use are generally oligonucleotides that are \`ink-jet printed` onto slides(Agilent) or synthesized in situ (Affymetrix). The amount of hybridisation detected for a specific probe is proportional to the number of nucleic acid fragments in the sample.

Replicates are essential for reliably detecting differentially expressed genes in microarray experiments. In Expression Atlas, a minimum acceptable number of biological sample replicates (three) is enforced to ensure sufficient statistical power to detect differential expression.


### 2.1 One colour array

Measure the expression levels from each sample.

 In one colour microarrays, each sample is labelled and hybridised to a separate microarray and we get an absolute value of fluorescence for each probe.

### 2.2 Two colour array

Compare relative expression levels between a pair of samples.

 In two colour microarrays, two biological samples (experimental/test sample and control/reference sample) are labelled with different fluorescent dyes, usually Cyanine 3 (Cy3) and Cyanine 5 (Cy5). Equal amounts of labelled cDNA are then simultaneously hybridised to the same microarray chip. After this competitive hybridisation, the fluorescence measurements are made separately for each dye and represent the abundance of each gene in one sample (test sample, Cy5) relative to the other one (control sample, Cy3). The hybridisation data are reported as a ratio of the Cy5/Cy3 fluorescent signals at each probe.

 One issue for two-colour arrays is related to dye bias effects introduced by the slightly different chemistry of the two dyes. It is important to control for this dye bias in the design of your experiment, for example by using a dye swap design or a reference design.

 ### 2.3 Limitations of microarrays

 - reliance upon existing knowledge about the genome sequence.
 - high background levels owing to cross-hybridisation.
 - limited dynamic range of detection owing to both background and saturation signals.
 - comparing expression levels across different experiments is often difficult and can require complicated normalisation methods.

### 2.4 Analysis of microarray data

Microarrays can be used in many types of experiments including genotyping, epigenetics, translation profiling and gene expression profiling.

The analysis method can be list as follows.

- feature extraction
- quality control
- normalisation
- differential expression analysis
- biological interpretation of the results
- submission of data to a public database

#### 2.4.1 Feature extraction

Converting the scanned image of the microarray into quantifiable values and annotating it. The output of this process is raw data files that can be in binary or text format.

| Manufacturer | Typical raw data format |
| :----------: | :---------------------: |
| Affymetrix | .CEL(binary) |
| Agilent	| feature extraction file (tab-delimited text file per hybridisation) |
| GenePix (scanner)	| .gpr (tab-delimited text file per hybridisation)	| 
| Illumina	| .idat (binary) / txt (tab-delimited text matrix for all samples) |
| Nimblegen	| NimbleScan, .pair (tab-delimited text matrix for all samples)	|

After the feature extraction process, the data can be analysed. We use R to do this('oligo','limma' and 'lumi').

#### 2.4.2 Quality control

In Expression Atlas, quality control of data from all microarray technologies (Affymetrix, Agilent and Illumina) is done using the ‘arrayQualityMetrics’ R package.

#### 2.4.3 Normalisation

Normalisation of microarray data is used to control for technical variation between assays, while preserving the biological variation.

- Affymetrix microarray data is normalised using the ‘Robust Multi-Array Average’ (RMA) method within the ‘oligo’ package.
- Agilent microarray data is normalised using the ‘limma’ package: ‘quantile normalisation’ for one-colour microarray data.

#### 2.4.4 Differential expression analysis

The goal of differential expression analysis is to identify genes whose expression differs under different conditions. An important consideration for differential expression analysis is correction for multiple testing(Or easily increase the chance of false positive results).

the ‘limma’ package that is used to identify differentially expressed genes incorporates a method to correct for multiple testing.

#### 2.4.5 Biological interpretation of microarray data

#### 2.4.6 Submission of data to a public repository