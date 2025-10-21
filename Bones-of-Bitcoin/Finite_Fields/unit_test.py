from finite_fields import FiniteFields
field_1=FiniteFields(2,7)
field_2=FiniteFields(5,7)
field_3=FiniteFields(0,7)
field_4=FiniteFields(3,7)
print(field_1)
print(field_2)
print(field_1 == field_1)
print(field_1== field_2)
print(field_1 != field_2)
c=field_1+field_2
d=field_1-field_2
e=field_2*field_1
print(f'c: {c} d: {d} e: {e}')
print(c==field_3)
print(field_1*field_2==field_4)
print(field_1**5)
print(field_1/field_2)