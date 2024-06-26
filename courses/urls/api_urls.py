from django.urls import path

from courses.views.api_views import (AddReviewAPIView, ApprovedReviewsAPIView,
                                     CourseDetailAPIView, CoursesListAPIView,
                                     CourseSearchAPIView,
                                     ModerateReviewAPIView,
                                     ReviewDetailAPIView,
                                     ReviewModerationAPIView, )

urlpatterns = [
    path('courses/', CoursesListAPIView.as_view(), name='api_courses_detail'),
    path('courses/<int:pk>', CourseDetailAPIView.as_view(), name='api_course_detail'),
    path('courses/search', CourseSearchAPIView.as_view(), name='course_search'),
    path('reviews/<int:pk>', ReviewDetailAPIView.as_view(), name='api_review_detail'),
    path('courses/reviews/<int:course_id>', ApprovedReviewsAPIView.as_view(), name='api_approved_reviews_for_course'),
    path('courses/<int:pk>/add_review', AddReviewAPIView.as_view(), name='add_review'),
    path('review_moderation/', ReviewModerationAPIView.as_view(), name='review_moderation'),
    path('reviews/<int:pk>/moderate/', ModerateReviewAPIView.as_view(), name='moderate_review')
]
