# Your Task
# Create a variable:

# sentence = "  i am learning python  "
# Do this:
# Remove extra spaces using strip()
# Then convert it to title() case
# Then replace "Python" with "FastAPI"
# Print the final result

sentence = "  i am learning python  "

step1= sentence.strip()
step2=step1.title()
step3=step2.replace("python","FastAPI")
print(step3)