from matplotlib import pyplot as plt
try:
    fats = float(input("Fats: ")) 
    carbs = float(input("Carbs: "))  
    protein = float(input("Protein: "))          
    
except ValueError:
    print("Did not give an Integer as a value")
    exit()


protein_kcal = protein*4
carbs_kcal = carbs*4
fats_kcal = fats*9

total_kcals = protein_kcal+carbs_kcal+fats_kcal


macros = [protein_kcal, fats_kcal,carbs_kcal]
labels = ['Protein', 'Fats', 'Carbs']
colors = ['#ff9999', '#66b3ff', '#99ff99'] 

plt.pie(macros, labels=labels, colors=colors, autopct=lambda p: '{:.1f}%'.format(p), startangle=90)
plt.title(f'Total Calories: {total_kcals}', pad=20)
# Ensure pie chart is circular
plt.axis('equal')
plt.show()
