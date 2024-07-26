print("Your Password:\n"+ "".join([__import__("random").choice("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()?") for i in range(16)]))
