
create a environment -- conda create -n env_name python == 3.7 --> version name if you dont give this will take latest version

to check if we have base environemtn - conda env list

to activate particular env - conda activate <env_name>

once u are in the env_name - check if required libararies are available by typing - pip list

to install particluar libarary like pandas
    pip install pandas - this is for pandas
    pip install scikit-learn - this is for sklearn

while sending the file for some one we have to send

python file, pkl file along with that we have to send the list of libararies for that 

write pip freeze > requirment.txt this will have list of the ibraries

to install all of them from a file -- pip install -r requirment.txt and then press enter it will install all the libararies

