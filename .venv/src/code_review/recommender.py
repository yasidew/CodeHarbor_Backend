import joblib

class CodeRecommender :
    def __init__(self,  model_path):
        self.model = joblib.load(model_path)

    def recommend_refactoring(self, code_features):
        recommendation =  self.model.predict([code_features])
        return recommendation


if __name__ == "__main__":
    model_path = 'data/models/your_trained_model.pkl'
    code_features =  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    recommender = CodeRecommender(model_path)
    print(recommender.recommend_refactoring(code_features))