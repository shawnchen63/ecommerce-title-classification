from pathlib import Path
import json
import pickle
import pkg_resources

from joblib import dump, load
import numpy as np

from artifacts.utils.download import download_file_from_google_drive

def get_model(model_folder_path):

  models = []
  model_names = ["beautypipeline1.joblib", "fashionpipeline1.joblib", "mobilepipeline1.joblib"]
  for model_name in model_names:

    model_path = Path(model_folder_path,model_name)

    if not model_path.is_file():
      download_file_from_google_drive(model_name, model_path)

    models.append(load(model_path))

  return tuple(models)


class Model():

  def __init__(self):
    
    model_path = pkg_resources.resource_filename(__name__, 'artifacts')

    self.b_pipeline, self.f_pipeline, self.m_pipeline = get_model(model_path)
    #del self.f_pipeline
    #del self.b_pipeline
    with open(Path(model_path,'category_mapper.p'), 'rb') as fp:
      self.category_mapper = pickle.load(fp)

  def predict(self, query, category):
    
    if (category==1):
      pipeline = self.b_pipeline
    elif (category==2):
      pipeline = self.f_pipeline
    elif (category==3):
      pipeline = self.m_pipeline

    else:
      raise NotImplementedError

    query = np.expand_dims(np.array(query), axis=0)

    prediction_code = pipeline.predict(query)
    print(prediction_code)

    return self.category_mapper[prediction_code[0]]

if __name__ == '__main__':
  model = Model()
  print(model.predict(["iphone 10"], 3))

