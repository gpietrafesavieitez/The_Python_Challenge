import pickle

pickled = open("banner.p", "rb")

banner = pickle.load(pickled)

for j in banner:
    print("".join([i[1] * i[0] for i in j]))