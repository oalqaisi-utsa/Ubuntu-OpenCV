FROM oalqaisi/opencv-build:$(arm64 or ubuntu) AS build

FROM ubuntu AS base

LABEL name="Osamah Alqaisi" \
      email="osamah.alqaisi@my.utsa.edu"

RUN apt-get update && apt-get upgrade -y \
	&& apt-get -y install --no-install-recommends python3 python3-pip \
	&& pip3 install numpy \
	&& apt-get -qq autoremove \
	&& apt-get -qq clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& rm -rf /tmp/*

COPY --from=build /usr/local/include/opencv4 /usr/local/include/opencv4
COPY --from=build /usr/local/lib/python3.10/dist-packages/cv2 /usr/local/lib/python3.10/dist-packages/cv2
COPY --from=build /usr/local/lib/libopencv* /usr/local/lib/

RUN apt-get update \
	&& apt-get -y install --no-install-recommends libjpeg62 libpng16-16 libtiff5 \
	&& apt-get -qq autoremove \
	&& apt-get -qq clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& rm -rf /tmp/* \
	&& ldconfig
