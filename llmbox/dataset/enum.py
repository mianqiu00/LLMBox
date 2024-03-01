STEM_SUBJECTS = [
    'abstract_algebra', 'astronomy', 'college_biology', 'college_chemistry', 'college_computer_science',
    'college_mathematics', 'college_physics', 'computer_security', 'conceptual_physics', 'electrical_engineering',
    'elementary_mathematics', 'high_school_biology', 'high_school_chemistry', 'high_school_computer_science',
    'high_school_mathematics', 'high_school_physics', 'high_school_statistics', 'machine_learning'
]
HUMANITIES_SUBJECTS = [
    'formal_logic', 'high_school_european_history', 'high_school_us_history', 'high_school_world_history',
    'international_law', 'jurisprudence', 'logical_fallacies', 'moral_disputes', 'moral_scenarios', 'philosophy',
    'prehistory', 'professional_law', 'world_religions'
]
SOCIAL_SCIENCES_SUBJECTS = [
    'econometrics', 'high_school_geography', 'high_school_government_and_politics', 'high_school_macroeconomics',
    'high_school_microeconomics', 'high_school_psychology', 'human_sexuality', 'professional_psychology',
    'public_relations', 'security_studies', 'sociology', 'us_foreign_policy'
]
OTHER_SUBJECTS = [
    'anatomy', 'business_ethics', 'clinical_knowledge', 'college_medicine', 'global_facts', 'human_aging', 'management',
    'marketing', 'medical_genetics', 'miscellaneous', 'nutrition', 'professional_accounting', 'professional_medicine',
    'virology'
]

MMLU_SUBJECTS = {
    'stem': STEM_SUBJECTS,
    'humanities': HUMANITIES_SUBJECTS,
    'social_sciences': SOCIAL_SCIENCES_SUBJECTS,
    'other': OTHER_SUBJECTS
}

BBH_PROMPTS = {
    'boolean_expressions': "Evaluate the result of a random Boolean expression.",
    'causal_judgement': "Answer questions about causal attribution.",
    'date_understanding': "Infer the date from context.",
    'disambiguation_qa': "Clarify the meaning of sentences with ambiguous pronouns.",
    'dyck_languages': "Correctly close a Dyck-n word.",
    'formal_fallacies': "Distinguish deductively valid arguments from formal fallacies.",
    'geometric_shapes': "Name geometric shapes from their SVG paths.",
    'hyperbaton': "Order adjectives correctly in English sentences.",
    'logical_deduction_five_objects': "A logical deduction task which requires deducing the order of a sequence of objects.",
    'logical_deduction_seven_objects': "A logical deduction task which requires deducing the order of a sequence of objects.",
    'logical_deduction_three_objects': "A logical deduction task which requires deducing the order of a sequence of objects.",
    'movie_recommendation': "Recommend movies similar to the given list of movies.",
    'multistep_arithmetic_two': "Solve multi-step arithmetic problems.",
    'navigate': "Given a series of navigation instructions, determine whether one would end up back at the starting point.",
    'object_counting': "Questions that involve enumerating objects and asking the model to count them.",
    'penguins_in_a_table': "Answer questions about a table of penguins and their attributes.",
    'reasoning_about_colored_objects': "Answer extremely simple questions about the colors of objects on a surface.",
    'ruin_names': "Select the humorous edit that 'ruins' the input movie or musical artist name.",
    'salient_translation_error_detection': "Detect the type of error in an English translation of a German source sentence.",
    'snarks': "Determine which of two sentences is sarcastic.",
    'sports_understanding': "Determine whether an artificially constructed sentence relating to sports is plausible or not.",
    'temporal_sequences': "Task description: Answer questions about which times certain events could have occurred.",
    'tracking_shuffled_objects_five_objects': "A task requiring determining the final positions of a set of objects given their initial positions and a description of a sequence of swaps.",
    'tracking_shuffled_objects_seven_objects': "A task requiring determining the final positions of a set of objects given their initial positions and a description of a sequence of swaps.",
    'tracking_shuffled_objects_three_objects': "A task requiring determining the final positions of a set of objects given their initial positions and a description of a sequence of swaps.",
    'web_of_lies': "Evaluate a random boolean function expressed as a word problem.",
    'word_sorting': "Sort a list of words."
}

BBH_NO_CHOICE = [
    'dyck_languages',
    'multistep_arithmetic_two',
    'object_counting',
    'word_sorting'
]
