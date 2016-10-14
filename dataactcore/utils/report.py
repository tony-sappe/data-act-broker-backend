def getReportPath(job, reportType):
    """
    Return the filename for the error report.
    Does not include the folder to avoid conflicting with the S3 getSignedUrl method.
    """
    path = 'submission_{}_{}_{}_report.csv'.format(job.submission_id, job.file_type.name, reportType)
    return path