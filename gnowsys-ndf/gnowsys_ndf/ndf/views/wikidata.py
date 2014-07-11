from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from gnowsys_ndf.ndf.models import *
from django_mongokit import get_database
from django.template import RequestContext

database = get_database()
collection = database[Node.collection_name]

def index(request, group_id):
	ins_objectid  = ObjectId()
    	if ins_objectid.is_valid(group_id) is False :
        	group_ins = collection.Node.find_one({'_type': "Group","name": group_id})
        	auth = collection.Node.one({'_type': 'Author', 'name': unicode(request.user.username) })
      	if group_ins:
       		group_id = str(group_ins._id)
      	else :
        	auth = collection.Node.one({'_type': 'Author', 'name': unicode(request.user.username) })
        if auth :
         	group_id = str(auth._id)
    	else :
        	pass

	selected_topic = None
	topic_coll = collection.Node.find({"_type": u"GSystem"})
	print "here: " + str(topic_coll)	
	context = RequestContext(request, {'title': "WikiData Topics", 'topic_coll': topic_coll})
	template = "ndf/wikidata.html"
     	variable = RequestContext(request,{'title': "WikiData Topics"})
	context_variables = {'title': "WikiData Topics"}
	context_instance = RequestContext(request, {'title': "WikiData Topics", 'groupid':group_id, 'group_id':group_id})
	attribute_set = None
      	return render(request, template, {'title': "WikiData Topics", 'topic_coll': topic_coll, 'selected_topic': selected_topic, 'attribute_set' : attribute_set, 'groupid':group_id, 'group_id':group_id})


def details(request, group_id, topic_id):
	ins_objectid  = ObjectId()
	group_ins = None
    	if ins_objectid.is_valid(group_id) is False :
        	group_ins = collection.Node.find_one({'_type': "Group","name": group_id})
        	auth = collection.Node.one({'_type': 'Author', 'name': unicode(request.user.username) })
      	if group_ins:
       		group_id = str(group_ins._id)
      	else :
        	auth = collection.Node.one({'_type': 'Author', 'name': unicode(request.user.username) })
        if auth :
         	group_id = str(auth._id)
    	else :
        	pass

	selected_topic = collection.Node.one({"_type":u"GSystem", "_id":ObjectId(topic_id)})
	topic_coll = collection.Node.find({"_type": u"GSystem"})
	print "here: " + str(topic_coll)	
	context = RequestContext(request, {'title': "WikiData Topics", 'topic_coll': topic_coll})
	template = "ndf/wikidata.html"
     	variable = RequestContext(request,{'title': "WikiData Topics"})
	context_variables = {'title': "WikiData Topics"}
	context_instance = RequestContext(request, {'title': "WikiData Topics", 'groupid':group_id, 'group_id':group_id})
	attribute_set = collection.Node.find({"_type":u"GAttribute", "subject":ObjectId(topic_id)})
	relation_set = collection.Node.find({"_type":u"GRelation", "subject":ObjectId(topic_id)})	
	print attribute_set
      	return render(request, template, {'title': "WikiData Topics", 'topic_coll': topic_coll, 'selected_topic': selected_topic, 'attribute_set': attribute_set,'relation_set':relation_set, 'groupid':group_id, 'group_id':group_id})




def tag_view_list(request, group_id, tag):
	ins_objectid  = ObjectId()
	group_ins = None
    	if ins_objectid.is_valid(group_id) is False :
        	group_ins = collection.Node.find_one({'_type': "Group","name": group_id})
        	auth = collection.Node.one({'_type': 'Author', 'name': unicode(request.user.username) })
      	if group_ins:
       		group_id = str(group_ins._id)
      	else :
        	auth = collection.Node.one({'_type': 'Author', 'name': unicode(request.user.username) })
        if auth :
         	group_id = str(auth._id)
    	else :
        	pass

	#selected_topic = collection.Node.one({"_type":u"GSystem", "_id":ObjectId(topic_id)})
	all_topic = collection.Node.find({"_type": u"GSystem"})
	topic_coll=[]	
	for topic in all_topic:
		if tag in topic.tags:
			topic_coll.append(topic)

	
	context = RequestContext(request, {'title': "WikiData Topics", 'topic_coll': topic_coll})
	template = "ndf/wikidata.html"
     	variable = RequestContext(request,{'title': "WikiData Topics"})
	context_variables = {'title': "WikiData Topics"}
	context_instance = RequestContext(request, {'title': "WikiData Topics", 'groupid':group_id, 'group_id':group_id})
	attribute_set = collection.Node.find({"_type":u"GAttribute", "subject":ObjectId(topic_id)})
	relation_set = collection.Node.find({"_type":u"GRelation", "subject":ObjectId(topic_id)})	
	print attribute_set
      	return render(request, template, {'title': "WikiData Topics", 'topic_coll': topic_coll, 'selected_topic': selected_topic, 'attribute_set': attribute_set,'relation_set':relation_set, 'groupid':group_id, 'group_id':group_id})


