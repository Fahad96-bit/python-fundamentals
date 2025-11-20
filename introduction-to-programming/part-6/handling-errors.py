# try { risky only }
# except { error }
# else { success code }
# finally { cleanup }


# ✅ JS vs Python error handling mindset
# JavaScript (generic catch)
# try {
#    // code
# } catch (err) {
#    console.log(err);
# }


# catch catches ANY error

# You decide inside the catch what to do

# JS doesn’t force you to separate error types.

# ✅ Python is more strict

# Python encourages saying what type of error you expect:

# try:
#     # code
# except ValueError:
#     print("Wrong value")
# except ZeroDivisionError:
#     print("You divided by zero")


# Why?
# Because Python believes:

# If you know what errors can happen, catch only those. Don’t hide everything.

# 🔥 So can Python catch all errors like JS?

# YES!

# You can catch any error generically:

# try:
#     # risky code
# except Exception as e:
#     print("Something went wrong:", e)


# This is the Python equivalent of JavaScript’s catch-all.
