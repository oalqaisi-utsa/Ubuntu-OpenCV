FROM oalqaisi/opencv-build:armv7 AS build

FROM ubuntu AS base

LABEL name="Osamah Alqaisi" \
      email="osamah.alqaisi@my.utsa.edu"

RUN apt-get update && apt-get upgrade -y \
	&& apt-get -y install --no-install-recommends \
	build-essential python3 python3-pip python3-dev ninja-build \
	&& pip3 install cython numpy

COPY --from=build /usr/local/include/opencv4 /usr/local/include/opencv4
COPY --from=build /usr/local/lib/python3.10/dist-packages/cv2 /usr/local/lib/python3.10/dist-packages/cv2
COPY --from=build /usr/local/lib/libopencv* /usr/local/lib/

RUN apt-get update \
	&& apt-get -y install --no-install-recommends libjpeg62 libpng16-16 libtiff5 \
	&& apt-get purge build-essential ninja-build python3-dev \
	&& pip3 uninstall cython \
	&& apt-get -qq autoremove \
	&& apt-get -qq autoclean \
	&& apt-get -qq clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& rm -rf /tmp/* \
	&& ldconfig
