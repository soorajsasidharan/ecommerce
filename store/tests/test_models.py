from email.mime import image
from itertools import product
from django.test import TestCase
from store.models import Category,Product
from django.contrib.auth.models import User

class TestCategoryModel(TestCase):
    def setUp(self):
        self.data1=Category.objects.create(name='django',slug='django')

    def test_category_model_entry(self):
        '''
        '''
        data = self.data1
        self.assertTrue(isinstance(data,Category))

    def test_category_model_entry(self):
        '''
        '''
        data = self.data1
        self.assertEqual(str(data),'django')


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django',slug='django')
        User.objects.create(username='admin')
        self.data1=product.objects.create(category_id=1,title='django_beginners',created_by_id=1,slug='django_beginners',price='20.00',image='django')


    def test_product_model_entry(self):
        data=self.data1
        self.assertTrue(isinstance(data,product))
        self.assertEqual(str(data),'django_biginnerd')

