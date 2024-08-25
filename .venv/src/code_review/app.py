from flask import Flask, request, jsonify
from src.analyzer import CodeAnalyzer
from src.checker import SecurityChecker, PerformanceChecker
from src.recommender import CodeRecommender

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_code():
    data = request.json
    code = data['code']

    #run code analysis
    analyzer = CodeAnalyzer(code)
    analyzer.run_pylint()
    analyzer.custom_rules_check()

    #run security checks
    sec_checker =  SecurityChecker(code)
    perf_checker = PerformanceChecker(code)
    sec_checker.check_insecure_imports()
    perf_checker.check_heavy_loops()

    #Generate code recommendations
    model_path = 'data/models/your_trained_model.pkl'
    recommender = CodeRecommender(model_path)

    #Example feature extraction from the code
    code_features= [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    recommendations = recommender.recommend_refactoring(code_features)

    return jsonify({
        'status': 'success',
        'recommendations': recommendations.tolist()
    })

if __name__ == '__main__':
    app.run(debug = True)
