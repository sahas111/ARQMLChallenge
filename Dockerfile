FROM  continuumio/miniconda3

ENV APP_HOME /ds-nlp-demo-sentiment-analysis
WORKDIR $APP_HOME
COPY . $APP_HOME

#Create a conda environment and install the packages defined in YAML file
RUN conda update --name base conda &&\
    conda env create --file environment.yml

EXPOSE 5000

SHELL ["conda", "run", "--name", "ds-nlp-demo-sentiment-analysis", "/bin/bash", "-c"]
ENTRYPOINT ["conda", "run", "--name", "ds-nlp-demo-sentiment-analysis", "python", "app.py"]
