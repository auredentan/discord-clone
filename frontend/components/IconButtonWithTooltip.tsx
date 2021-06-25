import React from 'react'

import { IconButton, Tooltip } from '@chakra-ui/react'

interface IconButtonWithTooltipProps {
	icon: React.ReactElement
	label: string
	ariaLabel: string
	onClick: () => void
}
const IconButtonWithTooltip = ({
	icon,
	onClick,
	label,
	ariaLabel,
}: IconButtonWithTooltipProps) => {
	return (
		<Tooltip label={label} aria-label={ariaLabel}>
			<IconButton onClick={onClick} aria-label={ariaLabel} icon={icon} />
		</Tooltip>
	)
}

export default IconButtonWithTooltip
