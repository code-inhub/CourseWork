def categorize_tuple_elements(input_tuple):
    int_elements = tuple(item for item in input_tuple if isinstance(item, int) and not isinstance(item, bool))
    float_elements = tuple(item for item in input_tuple if isinstance(item, float))
    str_elements = tuple(item for item in input_tuple if isinstance(item, str))
    bool_elements = tuple(item for item in input_tuple if isinstance(item, bool))

    return int_elements, float_elements, str_elements, bool_elements

input_tuple = (10, 3.14, "Hello", True, 42, "World", 3.14159, False)

int_elements, float_elements, str_elements, bool_elements = categorize_tuple_elements(input_tuple)

sorted_int = tuple(sorted(int_elements))
sorted_float = tuple(sorted(float_elements))
sorted_str = tuple(sorted(str_elements))
sorted_bool = tuple(sorted(bool_elements))

print("Integer Elements:", sorted_int)
print("Float Elements:", sorted_float)
print("String Elements:", sorted_str)
print("Boolean Elements:", sorted_bool)
