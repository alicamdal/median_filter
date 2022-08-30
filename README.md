# Median Filter for Distorted Sounds
Median filter is a non-linear digital filter method. This repo contains one dimensional median filter for degraded sounds. Filtering process is based on changing distorted value with the median value of the sequence. More information can be found [Justosson's article](https://link.springer.com/chapter/10.1007/BFb0057597).
 
## Installing Libraries
All required libraries can be found in requirements.txt
```
pip3 install -r requirements.txt
```
## Degradation and Detection Scripts
Filter needs degraded sound file and the binary file of the positions of distortion. These files can be created using degradation.py and detection.py which are located under the scripts folder.
Clean .wav file can be degraded with the certain number of noise. Details can be found in degradation.py
The positions of the distortion can be located using detection.py script. This script takes degraded .wav file and find the positions. Output of the detection script is a binary file with the extension of .raw.

## Example Usage for Median Filter
Filter takes several arguments. These are input file, detection binary file, filter size, and output file name respectively.
```
python3 median_filter.py input_file.wav detection.raw 15 output.wav
```
