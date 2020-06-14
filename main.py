import scraper
import ahfod
from itertools import permutations
from pprint import pprint 


palettes = scraper.get_palettes('https://www.color-hex.com/color-palettes/popular.php')

salmon = palettes['Facebook Messenger 1']
# salmon.reverse()
# pprint(salmon)
comb = permutations(salmon, 5)
pprint(list(list(comb)[0]))

# img = ahfod.top_down(1024, 768, salmon)
# img.show()
# img.save('imgs/SpringDays_TD.png')