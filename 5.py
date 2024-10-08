companies = ["Google", "Microsoft", "Amazon", "Flipkart", "Adobe"]
print(companies)

companies.append("Infosys")
print(companies)

companies.insert(1, "Wipro")
print(companies)

companies.remove("Microsoft")
print(companies)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0], sum(matrix[0]))
print(matrix[1], sum(matrix[1]))
print(matrix[2], sum(matrix[2]))