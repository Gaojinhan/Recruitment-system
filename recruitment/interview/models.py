from django.db import models

# Create your models here.

# First round result
FIRST_INTERVIEW_RESULT_TYPE = (('Pass', 'Pass'), ('Hold', 'Hold'), ('Reject', 'Reject'))

# Second round result
INTERVIEW_RESULT_TYPE = (('Pass', 'Pass'), ('Hold', 'Hold'), ('Reject', 'Reject'))

# Candidate eduction level
DEGREE_TYPE = (('Bachelor', 'Bachelor'), ('Master', 'Master'), ('Phd', 'Phd'))

# HR final result
HR_SCORE_TYPE = (('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'))

class Candidate(models.Model):
    # Basic information
    userid = models.IntegerField(unique=True, blank=True, null=True, verbose_name=u'Candidate Id')
    username = models.CharField(max_length=135, verbose_name=u'Name')
    city = models.CharField(max_length=135, verbose_name=u'City')
    phone = models.CharField(max_length=135, verbose_name=u'Phone Number')
    email = models.EmailField(max_length=135, blank=True, verbose_name=u'Email')
    apply_position = models.CharField(max_length=135, blank=True, verbose_name=u'Position')
    born_address = models.CharField(max_length=135, blank=True, verbose_name=u'Hometown')
    gender = models.CharField(max_length=135, blank=True, verbose_name=u'Gender')
    Candidate_remark = models.CharField(max_length=135, blank=True, verbose_name=u'Remark')

    # Education Background
    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name=u'Bachelor School')
    master_school = models.CharField(max_length=135, blank=True, verbose_name=u'Master School')
    doctor_school = models.CharField(max_length=135, blank=True, verbose_name=u'Doctor School')
    major = models.CharField(max_length=135, blank=True, verbose_name=u'Major')
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name=u'Degree')

    # Grade of general ability and paper test
    test_score_of_general_ability = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True,
                                                        verbose_name=u'General Test Score')
    paper_score = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True,
                                      verbose_name=u'Paper Test Score')

    # First round interview
    first_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name=u'First Score')
    first_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                 verbose_name=u'Learning Ability Score')
    first_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                        verbose_name=u'Professional Score')
    first_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'Advantages')
    first_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'Disadvantages')
    first_result = models.CharField(max_length=256, choices=FIRST_INTERVIEW_RESULT_TYPE, blank=True,
                                    verbose_name=u'First Result')
    first_recommend_position = models.CharField(max_length=256, blank=True, verbose_name=u'First Recommend Position')
    first_interviewer = models.CharField(max_length=256, blank=True, verbose_name=u'First Interviewer')
    first_remark = models.CharField(max_length=135, blank=True, verbose_name=u'First Remark')

    # Second round interview
    second_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                       verbose_name=u'Second Score')
    second_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                  verbose_name=u'Second Learning Ability')
    second_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                         verbose_name=u'Second Professional Competency')
    second_pursue_of_excellence = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                      verbose_name=u'Pursue Of Excellence')
    second_communication_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                       verbose_name=u'Communication Ability')
    second_pressure_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                verbose_name=u'Pressure Score')
    second_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'Second Interview Advantage')
    second_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'Second Interview Disadvantage')
    second_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True,
                                     verbose_name=u'Second Result')
    second_recommend_position = models.CharField(max_length=256, blank=True,
                                                 verbose_name=u'Second Interview Recommend Position')
    second_interviewer = models.CharField(max_length=256, blank=True, verbose_name=u'Second Interviewer')
    second_remark = models.CharField(max_length=135, blank=True, verbose_name=u'Second Interview Remark')

    # HR终面
    hr_score = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u'Final Score')
    hr_responsibility = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True,
                                         verbose_name=u'Final Score Of Responsibility')
    hr_communication_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True,
                                                verbose_name=u'Final Score Of Communication Ability')
    hr_logic_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True,
                                        verbose_name=u'Final Score Of Ability')
    hr_potential = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True,
                                    verbose_name=u'Final Score Of Potential')
    hr_stability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True,
                                    verbose_name=u'Final Score Of Stability')
    hr_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'Final Score Of Advantage')
    hr_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'Final Score Of Disadvantage')
    hr_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True,
                                 verbose_name=u'Final Score Of Result')
    hr_interviewer = models.CharField(max_length=256, blank=True, verbose_name=u'Final Test Interviewer')
    hr_remark = models.CharField(max_length=256, blank=True, verbose_name=u'Final Score Of Remark')

    creator = models.CharField(max_length=256, blank=True, verbose_name=u'Final Test Creator')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=u'Final Test Created Date')
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=u'Final Test Modified Date')
    last_editor = models.CharField(max_length=256, blank=True, verbose_name=u'Last Editor')

    class Meta:
        db_table = u'candidate'
        verbose_name = u'Applicant'
        verbose_name_plural = u'Applicants'


    # Python 2
    def __unicode__(self):
        return self.username

    # Python 3
    def __str__(self):
        return self.username