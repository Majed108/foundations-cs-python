def addTuples(tup1, tup2):
    # Initializing an empty list to store the sums
    sum_list = []
    
     #Iterating over the elements of the tuples
    for i in range(len(tup1)):
        # Adding the corresponding elements and appending to the list
        sum_list.append(tup1[i] + tup2[i])
    
     #Converting the list to a tuple and returning
    return tuple(sum_list)


print(addTuples((1,2,3),(4,5,6)))






def write_dict_to_json(dictionary, filename):
    json_str = "{\n"
    for key, value in dictionary.items():
        json_str += f'  "{key}": '
        if isinstance(value, str):
            json_str += f'"{value}",\n'
        elif isinstance(value, bool):
            json_str += f'{str(value).lower()},\n'
        elif isinstance(value, (int, float)):
            json_str += f'{value},\n'
        elif isinstance(value, dict):
            json_str += f'{write_dict_to_json(value, "")},\n'
        else:
            raise ValueError(f"Unsupported data type: {type(value)}")
    json_str = json_str.rstrip(",\n") + "\n}"
    
    with open(filename, 'w') as f:
        f.write(json_str)

# Test the function
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
write_dict_to_json(my_dict, 'output.json')






def json_to_dict(filename):
    with open(filename, 'r') as file:
        data = file.read()

    # Remove the outer square brackets
    data = data[1:-1]

    # Split the string into a list of JSON objects
    objects = data.split('},')

    # Add the closing bracket back to each JSON object
    objects = [obj + '}' for obj in objects[:-1]] + [objects[-1]]

    # Convert each JSON object to a dictionary
    list_of_dicts = []
    for obj in objects:
        # Remove the outer curly braces
        obj = obj[1:-1]

        # Split the string into a list of key-value pairs
        pairs = obj.split(',')

        # Convert each key-value pair to a dictionary entry
        dict_ = {}
        for pair in pairs:
            # Split the key and value
            key, value = pair.split(':')

            # Remove the quotes from the key and value
            key = key.strip()[1:-1]
            value = value.strip()[1:-1]

            # Add the key-value pair to the dictionary
            dict_[key] = value

        # Add the dictionary to the list
        list_of_dicts.append(dict_)

    return list_of_dicts

  
  



  