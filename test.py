import random
from tasks import add 
result = add.delay(random.randrange(1,100), random.randrange(1,100))
print result.get(timeout=0.5)
