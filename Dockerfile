FROM ubuntu:16.04
RUN  apt-get update
RUN  apt-get upgrade -y
# Install python3
RUN  apt-get install -y python3
# Install pip
RUN apt-get install -y wget vim
RUN wget -O /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py
RUN python3 /tmp/get-pip.py
RUN pip install --upgrade pip
#Install other libs
RUN pip install -U numpy
RUN pip install -U matplotlib
RUN pip install -U pandas
RUN pip install -U seaborn
RUN pip install -U scikit-learn

# Install python-dev
RUN apt-get update
RUN apt-get install -y python-dev
# Install jupyter notebook
RUN pip install  jupyter
RUN pip install  notebook