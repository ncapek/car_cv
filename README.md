# car_cv
CV project for interview

Two parts: color_classification and licence_plate

- color_classification:
	- task: write a scraper to gather car images and make a classifier to recognize the car's color
	- outlines
		- scraper was constructed and a total of 8940 cars were scraped, 1 image per car
		- dataset contains a single image from a frontal view under a 45 degree angle
		- most images contain the same background from a similar distance and angle
		- in some cases the images contain images of tyres or some other anomaly
		- looking at the images show that labels are likely incorrect in some cases and at times it's very difficult to differentiate between similar colors
		- the dataset is unbalanced in terms of car colors
		- data preprocessing included normalizing to (0,1) and converting images to histograms of pixel density
		- resampling was applied to make train set more balanced and didn't improve results too much
		- CNN was attempted
		- data augmentation was attempted
