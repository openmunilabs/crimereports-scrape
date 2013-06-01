import re

class CrimeDescription:
  def get_crime(self, data):
    result = { 
               'type': None, 
               'date': None,
               'location': None, 
               'description': None,
               'time': None,
               'perp': None,
               'address': None
             } 

    match = re.search("^(?P<type>.+), (?P<date>\d{2}/\d{2}/\d{2}), (?P<location>.*\d{2}), (?P<description>.*$)", data)
    result["type"] = match.group('type')
    result["date"] = match.group('date')
    result["location"] = match.group('location')
    result["description"] = match.group('description')
   
    result["address"] = self._get_address(result["location"]) 
    result["time"] = self._get_time(result["location"]) 
    result["perp"] = self._get_perp(result["description"]) 
    
    return result

  def is_equal(self, a, b):
    if a != b :
      print str(a) + " is not the same as " + str(b)

  def _get_address(self, location):
    city = "Arlington VA"
    result = location.replace(" block of ", " ")
    street =  re.sub(". At.*$", ", ", result) 

    address = street + city
    return address

  def _get_time(self, location):
    match = re.search("(?P<time>\d{1,2}:\d{2} [pa]m)", location)
    time =  match.group("time")
    return time


  def _get_perp(self, description):
    result = ""
    perp = re.search("(?P<perp>The subject is described as.*$)", description)

    if perp is not None:
      result = perp.group("perp")
    else:
      result = "There is no suspect(s) description." 

    return result

if __name__ == '__main__':
  data = "PEEPING TOM, 05/24/13, 2800 block of N. Clarendon Boulevard. At 7:50 pm on May 24, a male subject was peeping over the bathroom stall at female victims in the women&rsquo;s restroom. The subject fled the scene when the store manager called 911. The subject is described as a white male in his 40&rsquo;s, with shaggy brown hair. He was wearing a red t-shirt with a grey button down, blue jeans and was carrying a large green bag at the time of the incident."

  d = CrimeDescription()
  parsed = d.get_crime(data)
  d.is_equal("PEEPING TOM", parsed["type"])
  d.is_equal("05/24/13", parsed["date"])
  d.is_equal("2800 block of N. Clarendon Boulevard. At 7:50 pm on May 24", parsed["location"])
  d.is_equal("a male subject was peeping over the bathroom stall at female victims in the women&rsquo;s restroom. The subject fled the scene when the store manager called 911. The subject is described as a white male in his 40&rsquo;s, with shaggy brown hair. He was wearing a red t-shirt with a grey button down, blue jeans and was carrying a large green bag at the time of the incident.", parsed["description"])


  d.is_equal("2800 N. Clarendon Boulevard, Arlington VA", parsed["address"])
  d.is_equal("7:50 pm", parsed["time"])
  d.is_equal("The subject is described as a white male in his 40&rsquo;s, with shaggy brown hair. He was wearing a red t-shirt with a grey button down, blue jeans and was carrying a large green bag at the time of the incident.", parsed["perp"])
