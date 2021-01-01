# Covid-19-and-Pneumonia-detection-from-X-Ray
## POJECT TITLE
## COVID19 DETECTION USING X-RAY

## HOW CHEST X-RAY USED TO DETECT COVID19?

According to study, published in the May 14, 2020 issue of Radiology, identifies which patients may need to be hospitalized and intubated based on the severity of coronavirus patterns in the lungs seen in the X-rays, using a unique scoring system to evaluate severity. The results could help physicians more quickly identify, triage, and aggressively treat these high-risk patients.
 
Investigators focused on every patient's chest X-ray to examine patterns of coronavirus in their lungs, looking at the opacities (white circular markings associated with COVID) and where those patterns lay. Researchers divided the X-rays into six zones (upper right, upper left, middle right, middle left, lower right, and lower left) and developed a scoring system from zero to six to quantify severity. The total score depended on how many zones disease showed up in. Lower severity scores ranged from zero to two, and higher severity from three to six.



Top image: Chest radiograph of a 23-year-old male with no past medical history who tested positive for COVID-19 via RT-PCR and was subsequently discharged from the emergency department with home care and isolation precautions. Portable CXR shows right and left peripheral lower lung zone hazy opacities; total score=2.
Bottom image: Chest radiograph in a 32-year-old overweight (BMI=30) COVID-19 positive male with a history of childhood asthma who was subsequently admitted and intubated in the ICU for 3 days. Portable CXR shows opacities in all three right lung zones and in the left middle and lower lung zones; total score=5. Image courtesy of Mount Sinai Health System.

## HOW OUR MODEL WORKS?
Our model works on Deep Neural Networks in which there are different layers in each level, with dropout rate of 0.5 and we applied Softmax in the last dense layer of the network, and the Rectified Linear Unit(ReLu) is the rest others.
Model: "sequential_1"

Our model is basically predicting the results using Image processing with help of deep learning instead of using a 6 factor score due to which accuracy is about 80%, in image processing the model is trained on 201,870,340 parameters, in which it checks the opacity in different parts of the lungs.
Higher the opacity higher is the chance of being infected by COVID19.

IMPLEMENTATION OF OUR MODEL ON FLASK APP


## PACKAGES USED IN THE PROJECT:
Numpy
Tensorflow
Keras
Pandas
OS
Subprocess
Seaborn
Matplotlib
************************
