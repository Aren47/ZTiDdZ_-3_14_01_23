import base64
Text = input("Wpisz tekst: ")
example_input = Text
string_bytes = example_input.encode("ascii")
base64_bytes = base64.b64encode(string_bytes)
base64_string = base64_bytes.decode("ascii")
print(F"Zakodowane: {base64_string}")