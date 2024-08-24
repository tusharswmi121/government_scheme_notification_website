from flask import Flask, render_template, request

app = Flask(__name__)
# Define a list of dictionaries to store information about the government schemes
schemes = [
  {"name": "Pradhan Mantri Jan Dhan Yojana (PMJDY)", "age_min": 10, "age_max": 100, "gender": "male" or "female", "income_min": 0},
  {"name": "Pradhan Mantri Awas Yojana (PMAY)", "age_min": 18, "age_max": 65, "gender": "Male" or "Female", "income_min": 85000},
  {"name": "Deen Dayal Upadhyaya Grameen Kaushalya Yojana (DDU-GKY).", "age_min": 6, "age_max": 18, "gender": "male" or "Female", "income_min": 0},
  {"name": "National Rural Employment Guarantee Act (NREGA)", "age_min": 18, "age_max": 60, "gender": "male" or "female", "income_min": 0},
  {"name": "Pradhan Mantri Garib Kalyan Ann Yojana", "age_min": 18, "age_max": 60, "gender": "female", "income_min": 0},
  {"name": "Pradhan Mantri Sahaj Bijli Har Ghar Yojana", "age_min": 18, "age_max": 100, "gender": "male" or "female", "income_min": 10000},
  
  {"name": "Pradhan Mantri Garib Kalyan Yojana (PMGKY)", "age_min": 12, "age_max": 75, "gender": "male" or "female", "income_min": 0},
  {"name": "Mission Antyodaya", "age_min": 18, "age_max": 45, "gender": "male" or "female", "income_min": 80000},
  {"name": "Pradhan Mantri Kaushal Vikas Yojana", "age_min": 6, "age_max": 22, "gender": "male" or "female", "income_min": 0},
  {"name": "Deendayal Antyodaya yojana.", "age_min": 18, "age_max": 45, "gender": "male" or "female", "income_min": 0},
  {"name": "National Food Security Act (NFSA)", "age_min": 18, "age_max": 100, "gender": "female", "income_min": 34000},
  {"name": "Pradhan Mantri Ujjwala Yojana (PMUY)", "age_min": 20, "age_max": 60, "gender": "male" or "female", "income_min": 25000},

  {"name": "Atal Pension Yojana (APY)", "age_min": 65, "age_max": 150, "gender": "male" or "female", "income_min": 600000},
  {"name": "RURBAN", "age_min": 18, "age_max": 42, "gender": "male" or "female", "income_min": 100000},
  {"name": "Udaan.", "age_min": 6, "age_max": 16, "gender": "female", "income_min": 0},
  {"name": "Shyam Prasad Mukherjee RURban Mission.", "age_min": 45, "age_max": 60, "gender": "male", "income_min": 90000},
  {"name": "Antodaya Ann Yojana", "age_min": 5, "age_max": 60, "gender": "female", "income_min": 0},
  {"name": "Saubhagya", "age_min": 25 , "age_max": 60, "gender": "female", "income_min": 100000},

  {"name": "Standup India", "age_min": 10, "age_max": 20, "gender": "male" or "female", "income_min": 0},
  {"name": "Swachhgram", "age_min": 15, "age_max": 50, "gender": "male" or "female", "income_min": 0},
  {"name": "Pradhan Mantri Kaushal Yojana", "age_min": 6, "age_max": 14, "gender": "male" or "female", "income_min": 500},
  {"name": "Bio-energy schemes", "age_min": 26, "age_max": 45, "gender": "female", "income_min": 50000},
  {"name": "National Career Services.", "age_min": 18, "age_max": 45, "gender": "male" or "female", "income_min": 25000},
  {"name": "Pradhan Mantri Mudra Yojana", "age_min": 21, "age_max": 60, "gender": "male" or "female", "income_min": 31000},

  {"name": "PMGSY", "age_min": 25, "age_max": 35, "gender": "male", "income_min": 100000},
  {"name": "Pradhan Mantri YUVA Yojana.", "age_min": 16, "age_max": 26, "gender": "male" or "female", "income_min": 0},
  {"name": "Deendayal Upadhyay Grameen Kaushalya Yojana (DDU-GKY)", "age_min": 22, "age_max": 27, "gender": "male" or "female", "income_min": 2500},
  {"name": "Solar scheme", "age_min": 25, "age_max": 30, "gender": "female", "income_min": 35000},
  {"name": "Saubhagya", "age_min": 28, "age_max": 36, "gender": "female", "income_min": 46000},
]


# Define the selection criteria
# age = 30
# gender = "male"
# income = 500

# Filter the schemes based on the selection criteria

# Display the filtered schemes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    age = int(request.form['age'])
    salary = int(request.form['salary'])
    aadhaar = request.form['aadhaar']
    pan = request.form['pan']
    gender = request.form['gender']
    # for scheme in filtered_schemes:
    #   print(scheme["name"])
    filtered_schemes = [scheme for scheme in schemes if scheme["age_min"] <= age <= scheme["age_max"] and scheme["gender"] == gender and scheme["income_min"] <= salary]

    eligible = False

    if age >= 18 and salary >= 25000 and aadhaar != '' and pan != '':
        eligible = True

    return render_template('result.html', eligible=eligible, gender=gender,filtered_schemes=filtered_schemes)

if __name__ == '__main__':
    app.run(debug=True)