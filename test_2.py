from modules.functionality.identify_video_information import *

data = LinkInformation("https://www.youtube.com/playlist?list=PLgE5T8aQ-wrgA7K12vCZxifkh3b-xPvMt").get_metadata()
print(data)