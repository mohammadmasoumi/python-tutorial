data = {
    'name': 'asgharagha',
    'lastname': 'asghari',
    'age': 22,
    'grade': 20,
    'university': 'sharif university of technology' 
}

universities = [
    'sharif university of technology',
    'tehran university of technology'
]

# website/frontend -> backend validate

class DataValidation:

    def validate_name(self, name):
        if 'asghar' not in name:
            raise ValueError('you must be an asghar!')
        
        return 'Mr. ' + name

    def validate_age(self, age):
        if age < 0 or age > 100:
            raise ValueError('invalid age!')
        
        return age

    def validate_grade(self, grade):
        if not (0 <= grade <= 20):
            raise ValueError('invalid grade!')

        return grade

    def validate_university(self, university):
        if university not in universities:
            raise ValueError('sorry, we can provide you this service!')

        return university

    def __call__(self, data):
        validated_data = {}
        for key, value in data.items():
            validated_value = value
            f = getattr(self, f'validate_{key}', None) # defaultvalue: None
            if f is not None:
                validated_value = f(value)

            validated_data[key] = validated_value

        return validated_data

# validation = DataValidation()
# validation.validate_age(data.get('age'))

validation_cls = DataValidation()
validated_data = validation_cls(data=data)
print(f'validated_data: {validated_data}')