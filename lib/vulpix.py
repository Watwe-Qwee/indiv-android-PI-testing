import re
import json

def isEmail(PostData):
    EMAIL_PATTERN = r".*[_A-Za-z0-9-\\+]+((\\.|_)[_A-Za-z0-9-]+)*@"+"[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})"
    EMAIL_temp = re.compile(EMAIL_PATTERN)
    x = EMAIL_temp.search(PostData)
    if(x != None):
        return True
    return False
    
#including Audio/video
def isVideo(PostData):
    PostData = PostData.lower()
    FILE_PATTERN =r"((.+\.)(webm|mpg|mp2|mpeg|mpe|mpv|ogg|mp4|m4p|m4v|avi|wmv|mov|qt|flv|swf|avchd))"
    FILE_PATTERN_temp = re.compile(FILE_PATTERN)
    x = FILE_PATTERN_temp.search(PostData.lower())
    if(x != None):
        return True
    return False

def isAudio(PostData):
    PostData = PostData.lower()
    FILE_PATTERN =r"((.+\.)(mp3|wma|wav|mp2|aac|ac3|au|ogg|flac))"
    FILE_PATTERN_temp = re.compile(FILE_PATTERN)
    x = FILE_PATTERN_temp.search(PostData.lower())
    if(x != None):
        return True
    return False
    
def isPhoto(PostData):
    PostData = PostData.lower()
    FILE_PATTERN =r"((.+\.)(jpg|png|ico|gif|bmp|jpeg))"
    FILE_PATTERN_temp = re.compile(FILE_PATTERN)
    x = FILE_PATTERN_temp.search(PostData.lower())
    if(x != None):
        return True
    return False


# def isZipCode(PostData):
    
#     ZIPCODE_PATTERN = r"\\d{5}(-\\d{4})?"
#     ZIPCODE_PATTERN_temp = re.compile(ZIPCODE_PATTERN)
#     x = ZIPCODE_PATTERN_temp.search(PostData)
#     if(x != None):
#         return True
    
    
# def isCreditCard(PostData):
#     CREDIT_PATTERN = r"(?:(?<visa>\b4[0-9]{12}(?:[0-9]{3})?\b)|"+ "(?<mastercard>\b5[1-5][0-9]{14}\b)|"+ "(?<discover>\b6(?:011|5[0-9]{2})[0-9]{12}\b)|"+ "(?<amex>\b3[47][0-9]{13}\b)|"+ "(?<diners>\b3(?:0[0-5]|[68][0-9])?[0-9]{11}\b)|"+ "(?<jcb>\b(?:2131|1800|35[0-9]{3})[0-9]{11}\b))"
#     CREDIT_PATTERN_temp = re.compile(CREDIT_PATTERN)
#     x = CREDIT_PATTERN_temp.search(PostData)
#     if(x != None):
#         return True


def isLocationGPS(PostData):
    PostData = PostData.upper()
    temp_list = re.findall(r'[^\w\s]+|\w+', PostData)
    Loc_list = ["LAT","LONG","LNG","LATITUDE","LONGITUDE","LATLONG","GPS","COORDINATES","LOC"]
    for latlong in Loc_list:
        if latlong in temp_list:
            return True
        return False

        
def isIP(PostData):
    PostData = PostData.lower()
    ipv4Pattern = r"(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.){3}([01]?\\d\\d?|2[0-4]\\d|25[0-5])"
    ipv6Pattern = r"([0-9a-f]{1,4}:){7}([0-9a-f]){1,4}";
    
    ipv4Pattern_temp = re.compile(ipv4Pattern)
    ipv6Pattern_temp = re.compile(ipv6Pattern)
    
    
    x = ipv4Pattern_temp.search(PostData)
    y = ipv6Pattern_temp.search(PostData)
    if x != None or y != None:
        return True
    return False
    
def isAdId(PostData):
    PostData = PostData.lower()
    AdIdPattern = r"[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"
    AdIdPattern_temp = re.compile(AdIdPattern)
    x = AdIdPattern_temp.search(PostData)
    if(x != None):
#         print(x.group())
        return True
    return False

    
def isTimeZone(PostData):
    PostData = PostData.upper()
    TimeZonePattern = r"^((19|20)[0-9][0-9])[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])[T]([01][1-9]|[2][0-3])[:]([0-5][0-9])[:]([0-5][0-9])([+|-]([01][0-9]|[2][0-3])[:]([0-5][0-9])){0,1}"
    TimeZonePattern_temp = re.compile(TimeZonePattern)
    x = TimeZonePattern_temp.search(PostData)
    if(x != None):
        return True
    return False

def isCountry(PostData):
    PostData = PostData.upper()
    temp_list = re.findall(r'[^\w\s]+|\w+', PostData)
    
    TH_country_list = ["BANGKOK","TH","THA","TH_TH","ASIA"]
    for country_code in TH_country_list:
        if country_code in temp_list:
            return True
    return False
    
    
def isMACAddr(PostData, MacAddr):
    
    mac_list = MacAddr.split(":")
    
    m0 = mac_list[0]
    m1 = mac_list[1]
    m2 = mac_list[2]
    m3 = mac_list[3]
    m4 = mac_list[4]
    m5 = mac_list[5]
    
    PostData = PostData.upper()
    temp_list = re.findall(r'[^\w\s]+|\w+', PostData)
    
    if (m0 in temp_list)and (m1 in temp_list) and(m2 in temp_list) and (m3 in temp_list) and (m4 in temp_list) and (m5 in temp_list):
        return True
    return False


def checkPrivayLeakage(PostData, MacAddr=None):

    output = {}

    output['Email'] = isEmail(PostData)
    output['Video'] = isVideo(PostData)
    output['Audio'] = isAudio(PostData)
    output['Photo'] = isPhoto(PostData)
    #isZipCode
    #isCreditCard
    output['LocationGPS'] = isLocationGPS(PostData)
    output['IP'] = isIP(PostData)
    output['AdId'] = isAdId(PostData)
    output['TimeZone'] = isTimeZone(PostData)
    output['Country'] = isCountry(PostData)
    if(MacAddr!=None): 
        output['MACAddr'] = isMACAddr(PostData, MacAddr)

    return output

background_traffic = ['graph.facebook.com',
        'play.googleapis.com',
        'android.googleapis.com',
        'www.googleapis.com',
        'android.clients.google.com',
        'connectivitycheck.gstatic.com',
        'clients3.google.com']

exact_field_dict = {
    "google_ad_id" : "Advertiser ID",
    "dvs" : "Device SN",
    "location_area_code" : "Location Area Code",
    "country" : "Country",
    "gender" : "Gender",
    "lastname" : "Name",
    "zip" : "Physical Address",
    "cty" : "Physical Address",
    "lat" : "GPS",
    "lon" : "GPS",
    "lng" : "GPS",
    "lat" : "GPS",
    "alt" : "GPS",
    "location" : "GPS",
    "imei" : "IMEI",
    "mac" : "MAC Address",
    "bssid" : "MAC Address",
    "cell" : "GSM Cell ID",
    "icc" : "ICCID",
    "imsi" : "IMSI"
}

PII_TYPE_2 = [ "Email", "Video", "Audio", "Photo",
                "LocationGPS", "IP", "AdId", "TimeZone", "Country", "MACAddr"]

PII_TYPE = [    "Advertiser ID", "Android ID", "Device SN",
                "GSF ID", "IMEI", "MAC Address",
                "GSM Cell ID", "ICCID", "IMSI",
                "Location Area Code", "Phone Number", "Age",
                "Audio", "Calendar", "Contract Book",
                "Country", "Date Of Birth", "Credit Card",
                "Email", "Gender", "Name",
                "Password", "Photo", "Physical Address",
                "Relationship", "SMS", "SSN",
                "Time Zone", "Username", "Video",
                "Web Log", "GPS" ]
    
def checkPrivacyLeakage(DumpedData, limit_header_length = 300, limit_content_length = 300):
    #Data Preparation
    if type(DumpedData) != type({}):
        DumpedData = DumpedData.get_state()

    request = DumpedData['request']
    host = request['host']
    headers = request['headers']

    output = {}

    if host in background_traffic:
        return output

    # Exact checking
    for (key, _) in headers:
        try:
            if key.decode().lower() in exact_field_dict:
                output[exact_field_dict[key.decode()]] = 1
        except:
            print("Can not decode.")

    content_type = None
            
    #Header checking and prepare content type
    for header in headers:
        try:
            temp_content_type = header[0].decode()
            if "content" in temp_content_type and "type" in temp_content_type:
                content_type = header[0].decode()
            for i in range(1,len(header)):
                temp_header = header[i].decode() if type(header[i]) is bytes else header[i]
                temp_header = temp_header.lower()
                if len(temp_header) < limit_header_length:
                    for (key, value) in checkPrivayLeakage(temp_header).items():
                        if value != 0 : output[key] = 1 
        except:
            print("Can not decode.")
    
    if "content" in request and content_type != None:
        content = request['content']
        if "json" in content_type:
            try:
                content = json.loads(str(content.decode()))
                for (key, value) in content.items():
                    if key in exact_field_dict:
                        output[exact_field_dict[key]] = 1
                    if len(value) < limit_content_length:
                        for (key1, value1) in checkPrivayLeakage(str(value).lower()).items():
                            if value1 != 0 : output[key1] = 1 
            except:
                print("Can not decode.")
        elif "image" in content_type:
            output["Photo"] = 1
        elif "video" in content_type:
            output["Video"] = 1
        else:
            try:
                content = content.decode()
                if len(content) < limit_content_length:
                    for (key1, value1) in checkPrivayLeakage(str(content).lower()).items():
                                if value1 != 0 : output[key1] = 1 
            except:
                 print("Can not decode.")

    return output
