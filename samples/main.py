from tasks import add

result = add.delay(66, 4)
print(result.id)
