#Write a function that merges two Python dictionaries. If a key exists in both, sum their values.
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Start with a copy of the first dictionary
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Sum the values if the key exists in both dictionaries
        else:
            merged_dict[key] = value  # Add the key-value pair if it doesn't exist in the first dictionary
    return merged_dict
print("Enter the first dictionary (key:value pairs separated by commas): ")
dict1_input = input()
dict1 = dict(item.split(":") for item in dict1_input.split(","))

print("Enter the second dictionary (key:value pairs separated by commas): ")
dict2_input = input()
dict2 = dict(item.split(":") for item in dict2_input.split(","))

result = merge_dicts(dict1, dict2)
print("Merged dictionary:", result)