import pickle
intbyte = []
strbyte = []

pickle.dump(intbyte, open("intbyte.TijnUtil", "wb"))
pickle.dump(strbyte, open("strbyte.TijnUtil", "wb"))
print("Done!")
