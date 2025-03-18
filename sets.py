students_ids = {'001', '002', '003', 'True', 'Mercy'}
students_list = (students_ids)
print(students_ids)
print(type(students_ids))


# ...existing code...

# Create another set of students
new_students = {'004', '005', 'Mercy', '001'}

# Demonstrate set operations
print("\nSet Operations:")

# Union - combines all unique elements
print("Union:", students_ids | new_students)

# Intersection - elements present in both sets
print("Intersection:", students_ids & new_students)

# Difference - elements in students_ids but not in new_students
print("Difference:", students_ids - new_students)

# Symmetric difference - elements in either set but not in both
print("Symmetric difference:", students_ids ^ new_students)

# Set methods
print("\nSet Methods:")
students_ids.add('006')  # Add a single element
print("After adding '006':", students_ids)

students_ids.update(['007', '008'])  # Add multiple elements
print("After updating:", students_ids)

# Check membership
print("\nMembership:")
print("Is '001' in the set?", '001' in students_ids)
print("Total number of students:", len(students_ids))