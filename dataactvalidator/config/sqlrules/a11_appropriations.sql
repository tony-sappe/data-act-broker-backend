WITH appropriation_a11_{0} AS 
	(SELECT submission_id,
		row_number,
		spending_authority_from_of_cpe,
		tas
	FROM appropriation
    WHERE submission_id = {0})
SELECT
    approp.row_number,
    approp.spending_authority_from_of_cpe,
    SUM(sf.amount) as sf_133_amount_sum
FROM appropriation_a11_{0} as approp
    INNER JOIN sf_133 as sf ON approp.tas = sf.tas
    INNER JOIN submission as sub ON approp.submission_id = sub.submission_id AND
        sf.period = sub.reporting_fiscal_period AND
        sf.fiscal_year = sub.reporting_fiscal_year
WHERE sf.line in (1750, 1850)
GROUP BY approp.row_number, approp.spending_authority_from_of_cpe
HAVING approp.spending_authority_from_of_cpe <> SUM(sf.amount)