CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

# install edj
ADD_CUSTOM_TARGET(classic-watch.edj
		COMMAND edje_cc -id ${CMAKE_CURRENT_SOURCE_DIR}/edje/images
		${CMAKE_CURRENT_SOURCE_DIR}/edje/classic-watch.edc classic-watch.edj
		DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/edje/classic-watch.edc
)
ADD_DEPENDENCIES(${PROJECT_NAME} classic-watch.edj)
INSTALL(FILES classic-watch.edj DESTINATION ${EDJDIR})

# install images
INSTALL(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/images/ DESTINATION ${IMAGEDIR} FILES_MATCHING PATTERN "*.png")
