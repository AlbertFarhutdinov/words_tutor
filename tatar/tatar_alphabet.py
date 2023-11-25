A_UPPER = chr(1240)
A_LOWER = chr(1241)
G_UPPER = chr(1174)
G_LOWER = chr(1175)
N_UPPER = chr(1186)
N_LOWER = chr(1187)
O_UPPER = chr(1256)
O_LOWER = chr(1257)
U_UPPER = chr(1198)
U_LOWER = chr(1199)
H_UPPER = chr(1210)
H_LOWER = chr(1211)

CONSONANTS = {
    'б', 'в', 'г', 'д', 'ж', G_LOWER, 'з', 'й', 'к', 'л', 'м', 'н', N_LOWER,
    'п', 'р', 'с', 'т', 'ф', 'х', H_LOWER, 'ц', 'ч', 'ш', 'щ',
}
VOWELS = {
    'а', A_LOWER, 'е', 'ё', 'и', 'о', O_LOWER, 'у',
    U_LOWER, 'ы', 'э', 'ю', 'я',
}

HARD_VOWELS = {'а', 'о', 'у', 'ы', 'э'}
SOFT_VOWELS = {A_LOWER, 'е', 'ё', 'и', O_LOWER, U_LOWER, 'ю', 'я'}
NASAL_CONSONANTS = {'м', 'н'}
