import re
from fastapi import HTTPException
def normalise_indian_mobile_number(mobile_number: str) -> str:

    #Remove whitespaces and common separators
    mobile_number = re.sub(r"[^\d+]","",mobile_number.strip())



    #handle 00 international prefix
    if mobile_number.startswith("00"):
        mobile_number = "+" + mobile_number[2:]

    #handle leading 0 (local format: 09xxxx)
    if mobile_number.startswith("0"):
        mobile_number = "+91" + mobile_number[1:]

    #handle 91xxxx without +
    if re.match(r"^91[6-9]\d{9}$",mobile_number):
        mobile_number = "+" + mobile_number

    #assume India if no country code
    if not mobile_number.startswith("+91"):
        mobile_number = "+91" + mobile_number

    #final validation

    if not re.match(r"^\+91[6-9]\d{9}", mobile_number):
        raise HTTPException(status_code=422, detail=f"Invalid Indian Phone number")

    return mobile_number



    return mobile_number