# from distutils.log import error
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This will get logged to a file')

# n = int(input())


# for i in range(1,n+1):
#     if i %2 ==0:
#         pass
#     else:
#         n = i+2
        
# print(n*n)
import logging
logging.basicConfig(filename='app.log', filemode='w',format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')
try:
    print(x)
except Exception as e:
    print(e) 
    # logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    # logging.info('Test LogInformation',e)
    logging.error("%s",e)
    logging.warning(e)