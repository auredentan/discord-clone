import React from 'react'

import { Grid, GridItem } from '@chakra-ui/react'

const Topbar = () => {
	return (
		<Grid templateColumns="repeat(6, 1fr)" gap={1}>
			<GridItem colSpan={1} h="10">
				<div>Server name</div>
			</GridItem>
			<GridItem colSpan={5} h="10">
				<div>Channel bar</div>
			</GridItem>
		</Grid>
	)
}

export default Topbar
