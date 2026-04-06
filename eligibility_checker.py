def check_eligibility(dept, marks):
      if marks < 0 or marks >  100: 
        return "Invalid Marks! PLease Enter Between 0-100."
      if dept == "engineering":
        if marks >= 70:
            return "Approved For Engineering"
        else:
            return "Rejected: Need At Least 70 In Maths."
      elif dept == "medical":
        if marks >= 80:
            return "Approved For Medcal!"
        else:
            return "Rejected: Need At Least 80 In Biology."
      else:
        return "Department Not Found! Please Choose Engineering or Medical."
print("--- University Asmission Portal ---")
try:
    dept_input = input("Enter Department (Engineering/Medical): ").lower()
    marks_input = int(input("Enter Your Marks: "))
    result = check_eligibility(dept_input, marks_input)
    print("\n--- Admission Status ---")
    print(result)
except ValueError:
    print("\nInvalid Input! Please Ensure You Enter Numbers Only.")

        


       