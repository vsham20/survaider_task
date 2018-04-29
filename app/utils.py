from models import IndividualDetails
from flask_paginate import Pagination
from flask import request
from app import cache

@cache.cached(timeout=60)
def fetch_gender_and_relationship_data():
    print "From db"
    count_per_gender = dict()
    male_count = IndividualDetails.objects.filter(gender="Male").count()
    female_count = IndividualDetails.objects.filter(gender="Female").count()
    count_per_gender['Male'] = male_count
    count_per_gender['Female'] = female_count
    return count_per_gender

@cache.cached(timeout=60)
def people_count_in_each_relationship():
    count_per_relation = dict()
    all_relations = IndividualDetails.objects.distinct('relationship')
    for relation in all_relations:
        count = IndividualDetails.objects.filter(relationship=relation).count()
        count_per_relation[relation] = count
    return count_per_relation

def get_all_data(request):
    filter1 = request.args.get('relationship')
    filter2 = request.args.get('race')
    filter3 = request.args.get('gender')
    query_filter = {}
    if filter1:
        query_filter['relationship'] = filter1
    if filter2:
        query_filter['race'] = filter2
    if filter3:
        query_filter['gender'] = filter3
    if query_filter.keys():
        all_data = IndividualDetails.objects.filter(**query_filter)
    else:
        all_data = IndividualDetails.objects.all()

    pagination, data, offset = for_pagination(all_data)
    return pagination, data, offset

def get_page_items():
    page = int(request.args.get('page', 1))
    per_page = request.args.get('per_page')
    if not per_page:
        per_page = 50
    else:
        per_page = int(per_page)

    offset = (page - 1) * per_page
    return page, per_page, offset

def for_pagination(object_list):
    page, per_page, offset = get_page_items()
    count = object_list.count()
    a = offset
    b = offset+per_page
    object_list = object_list[a:b]
    pagination = Pagination(page=page,
                per_page=per_page,
                total=count,
                css_framework='bootstrap3',
                show_single_page = False
                )
    return pagination,object_list,offset