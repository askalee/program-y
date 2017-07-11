import unittest
import os

from programy.config.file.xml_file import XMLConfigurationFile
from programy.config.sections.client.console import ConsoleConfiguration


class XMLConfigurationFileTests(unittest.TestCase):

    def test_load_from_file(self):
        xml = XMLConfigurationFile()
        self.assertIsNotNone(xml)
        xml.load_from_file(os.path.dirname(__file__)+"/test_xml.xml", ConsoleConfiguration(), ".")
        self.assertIsNotNone(xml.xml_data)
        brain = xml.get_section("brain")
        self.assertIsNotNone(brain)
        files = xml.get_section("files", brain)
        self.assertIsNotNone(files)
        aiml = xml.get_section("aiml", files)
        self.assertIsNotNone(aiml)

        # TODO Add tests to check values have been loaded

    def test_load_from_text(self):
        xml = XMLConfigurationFile()
        self.assertIsNotNone(xml)
        xml.load_from_text("""<?xml version="1.0" encoding="UTF-8" ?>
<root>
	<brain>
		<overrides>
			<allow_system_aiml>true</allow_system_aiml>
			<allow_learn_aiml>true</allow_learn_aiml>
			<allow_learnf_aiml>true</allow_learnf_aiml>
		</overrides>
		<defaults>
			<default-get>unknown</default-get>
			<default-property>unknown</default-property>
			<default-map>unknown</default-map>
			<learn-filename>y-bot-learnf.aiml</learn-filename>
		</defaults>
		<nodes>
			<pattern_nodes>$BOT_ROOT/config/pattern_nodes.conf</pattern_nodes>
			<template_nodes>$BOT_ROOT/config/template_nodes.conf</template_nodes>
		</nodes>
		<binaries>
			<save_binary>false</save_binary>
			<load_binary>false</load_binary>
			<binary_filename>$BOT_ROOT/output/y-bot.brain</binary_filename>
			<load_aiml_on_binary_fail>false</load_aiml_on_binary_fail>
			<dump_to_file>$BOT_ROOT/output/braintree.txt</dump_to_file>
		</binaries>
		<files>
			<aiml>
				<files>$BOT_ROOT/aiml</files>
				<extension>.aiml</extension>
				<directories>true</directories>
				<errors>$BOT_ROOT/output/y-bot_errors.txt</errors>
				<duplicates>$BOT_ROOT/output/y-bot_duplicates.txt</duplicates>
			</aiml>
			<sets>
				<files>$BOT_ROOT/sets</files>
				<extension>.txt</extension>
				<directories>false</directories>
			</sets>
			<maps>
				<files>$BOT_ROOT/maps</files>
				<extension>.txt</extension>
				<directories>false</directories>
			</maps>
			<denormal>$BOT_ROOT/config/denormal.txt</denormal>
			<normal>$BOT_ROOT/config/normal.txt</normal>
			<gender>$BOT_ROOT/config/gender.txt</gender>
			<person>$BOT_ROOT/config/person.txt</person>
			<person2>$BOT_ROOT/config/person2.txt</person2>
			<predicates>$BOT_ROOT/config/predicates.txt</predicates>
			<pronouns>$BOT_ROOT/config/pronouns.txt</pronouns>
			<properties>$BOT_ROOT/config/properties.txt</properties>
			<triples>$BOT_ROOT/config/triples.txt</triples>
			<preprocessors>$BOT_ROOT/config/preprocessors.conf</preprocessors>
			<postprocessors>$BOT_ROOT/config/postprocessors.conf</postprocessors>
		</files>
		<services>
			<REST>
				<classname>programy.utils.services.rest.GenericRESTService</classname>
				<method>GET</method>
				<host>0.0.0.0</host>
			</REST>
			<Pannous>
				<classname>programy.utils.services.pannous.PannousService</classname>
				<url>http://weannie.pannous.com/api</url>
			</Pannous>
			<Pandora>
				<classname>programy.utils.services.pandora.PandoraService</classname>
				<url>http://www.pandorabots.com/pandora/talk-xml</url>
			</Pandora>
			<Wikipedia>
				<classname>programy.utils.services.wikipediaservice.WikipediaService</classname>
			</Wikipedia>
		</services>
	</brain>
	<bot>
		<license_keys>$BOT_ROOT/config/license.keys</license_keys>
		<prompt>>>></prompt>
		<initial_question>Hi, how can I help you today?</initial_question>
		<default_response>Sorry, I don't have an answer for that!</default_response>
		<empty_string_srai>YEMPTY</empty_string_srai>
		<exit_response>So long, and thanks for the fish!</exit_response>
		<override_predicates>true</override_predicates>
		<max_recursion>10</max_recursion>
		<spelling>
			<classname>programy.utils.spelling.checker.SpellingChecker</classname>
			<corpus>$BOT_ROOT/spelling/corpus.txt</corpus>
			<check_before>true</check_before>
			<check_and_retry>false</check_and_retry>
		</spelling>
	</bot>
	<rest>
		<host>127.0.0.1</host>
		<port>5000</port>
		<debug>false</debug>
	</rest>
	<webchat>
		<host>127.0.0.1</host>
		<port>5000</port>
		<debug>false</debug>
	</webchat>
	<twitter>
		<polling>true</polling>
		<polling_interval>49</polling_interval>
		<streaming>false</streaming>
		<use_status>true</use_status>
		<use_direct_message>true</use_direct_message>
		<auto_follow>true</auto_follow>
		<storage>file</storage>
		<storage_location>$BOT_ROOT/storage/twitter.data</storage_location>
		<welcome_message>Thanks for following me, send me a message and I'll try and help</welcome_message>
	</twitter>
	<facebook>
		<polling>false</polling>
		<polling_interval>30</polling_interval>
		<streaming>true</streaming>
	</facebook>
	<xmpp>
		<server>talk.google.com</server>
		<port>5222</port>
		<xep_0030>true</xep_0030>
		<xep_0004>true</xep_0004>
		<xep_0060>true</xep_0060>
		<xep_0199>true</xep_0199>
	</xmpp>
</root>
""", ConsoleConfiguration(), ".")

        # TODO Add tests to check values have been loaded
