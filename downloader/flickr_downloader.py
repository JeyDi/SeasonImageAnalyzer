import multiprocessing
from PIL import Image
import flickrapi
import requests
import time
import os


class Download(object):
	LIMIT=10

	def __init__(self, data):
		# data is a tuple of list: ta=(['tag', 'text'],)
		# or a number
		if data:

			self.API = flickrapi.FlickrAPI(api_key='0687a10cb6c7dd42e4ca6faf7eebf1bd',
										   secret='0d61239106732ef1', format='etree',
										   token=False, store_token=False, timeout=3.0)
			self.pool = []
			self.multi(data)

	def multi(self, data):
		if type(data) is int:
			for x in range(data):
				process = multiprocessing.Process(group=None, target=self.download, name='SimProcess' + str(x),
											   args=('SimProcess' + str(x), None, None))
				self.pool.append(process)
				print(process)

		else:
			counter = 0
			for x in data:
				counter += 1
				process = multiprocessing.Process(group=None, target=self.download, name='PROCESS' + str(counter)+str(x),
											   args=x)
				print(process)
				self.pool.append(process)

		for x in self.pool:
			x.start()
			time.sleep(0.5)
			print(x)

	def download(self, *args):
		"""main crawler cicle for flickr"""

		print(multiprocessing.current_process().name)
		counter = 0
		skip_counter = 0

		try:
			for photo in self.API.walk(media='photos',
									   extras='url_o',
									   tag_mode='all',
									   content_type=1,
									   accuracy=1,
									   tags=args[0],
									   text=args[1]):

				#skip 10 elements
				skip_counter += 1

				if skip_counter == self.LIMIT:
					skip_counter=0

					"""download image file"""
					url = photo.get('url_o')
					if url is None:
						url = photo.get('url_l')
					if url is None:
						url = photo.get('url_c')
					if url is None:
						url = photo.get('url_z')


					#lot of images don't have public url

					if url is None:
						pass
					else:
						try:
							with open('Images/'+str(multiprocessing.current_process().name)+str(counter), 'wb') as file:

								print(str(multiprocessing.current_process().name)+' targeting element ', counter)
								file.write(requests.get(url, stream=True).content)
								file.close()
								img = Image.open('Images/'+str(multiprocessing.current_process().name) + str(counter))
								os.remove('Images/' + str(multiprocessing.current_process().name) + str(counter))
								img = img.convert('RGB')
								img = img.resize((224, 224), Image.ANTIALIAS)
								img.save('Images/'+str(multiprocessing.current_process().name)+str(counter) + '.jpg')
								counter += 1
						except Exception as err:
							print(err, ' error element ', counter, ', changing target')

					if counter > 200:
						break

		except Exception as err:
			print(err, ' thread is dead')


if __name__ == '__main__':
	dw = Download(
		data=(['landscape, summer', None], ['landscape, winter', None], ['landscape, autumn', None], ['landscape, spring', None],)
	)


