import pywhatkit as pwk
pwk.sendwhatmsg_instantly(
    phone_no="+79254101873",  # Include country code
    message="Hello from Python!",
    wait_time=15,  # Seconds to wait before sending
    tab_close=True  # Close browser tab after sending
)