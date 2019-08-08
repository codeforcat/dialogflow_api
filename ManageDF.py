import dialogflow_v2 as dialogflow
import uuid

class ManageDF():
    project_id = 'catbot-test-private-ide'
    client = None
    parent = None
    session_id = None
    def __init__(self):
        #session_client = dialogflow.SessionsClient()
        #self.session_id = session_client.session_path(self.project_id, '1')
        #print(self.session_id)
        self.session_client = dialogflow.SessionsClient()
        self.session_id = uuid.uuid4().hex
        self.session = self.session_client.session_path(self.project_id, self.session_id)
        print(self.session)
        self.client = dialogflow.IntentsClient()

        self.parent = self.client.project_agent_path(self.project_id)

    def _get_intent_list(self):
        parent = self.client.project_agent_path(self.project_id)
        intent_list = self.client.list_intents(parent)
        return intent_list

    def _get_intent(self,name):
        name = self.client.intent_path(self.project_id, name)
        response = self.client.get_intent(name)
        return response

    def _create_intent(self):
        params = dialogflow.types.Intent.Parameter(display_name='test4', value='test3', is_list=True)
        tp = dialogflow.types.Intent.TrainingPhrase()
        part = dialogflow.types.Intent.TrainingPhrase.Part(
            text="hope to register an traning phrase")
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])

        tp.Part(entity_type='@tes4_type', alias='test_alias', user_defined=True,text='test4istest4')
        t = dialogflow.types.Intent.Message.Text(text=['Hello world'])
        m = dialogflow.types.Intent.Message(text=t)

        new_intent = dialogflow.types.Intent(
            display_name='test4',
            messages=[m],
            training_phrases=[training_phrase],
            parameters=[params]
            )

        result = self.client.create_intent(self.parent,new_intent)


    def add_intent(self,itemdic):
        pass

    def update_intent(self):
        pass

    def delete_intent(self):
        pass

    #def create_entity(self,project_id, entity_type_id, entity_value, synonyms):
    def create_entity(self):
        entity_values = ['amagami','amagami2']
        display_name = 'testentity'
        self._create_session_entity_type(self.project_id,"c0c41483cfdd44b49cd60814494c89b3",entity_values,display_name,1)

    def _create_session_entity_type(self,project_id, session_id, entity_values,
                                   entity_type_display_name, entity_override_mode):
        """Create a session entity type with the given display name."""

        session_entity_types_client = dialogflow.SessionEntityTypesClient()

        session_path = session_entity_types_client.session_path(
            project_id, session_id)
        session_entity_type_name = (
            session_entity_types_client.session_entity_type_path(
                project_id, session_id, entity_type_display_name))

        # Here we use the entity value as the only synonym.
        entities = [
            dialogflow.types.EntityType.Entity(value=value, synonyms=[value])
            for value in entity_values]
        session_entity_type = dialogflow.types.SessionEntityType(
            name=session_entity_type_name,
            entity_override_mode=entity_override_mode,
            entities=entities)

        response = session_entity_types_client.create_session_entity_type(
            session_path, session_entity_type)

        print('SessionEntityType created: \n\n{}'.format(response))



    def update_entity(self):
        pass

    def delete_entity(self):
        pass



if __name__ == '__main__':
    mdf = ManageDF()
    #mdf._create_intent()
    mdf.create_entity()


    #print(mdf._get_intent('010bc69b-97c3-4bc3-ab51-71cb6fb3c8d3'))
    #print(mdf.get_intent_list())
    #intent_list = mdf._get_intent_list()
    # for item in mdf._get_intent_list():
    #    #print(item.name)
    #     if item.parameters:
    #         print(item.name,item.parameters[0])
