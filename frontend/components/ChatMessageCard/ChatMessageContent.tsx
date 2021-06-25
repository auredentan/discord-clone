import { CheckIcon, CloseIcon, EditIcon } from '@chakra-ui/icons'
import {
	ButtonGroup,
	Editable,
	EditableInput,
	EditablePreview,
	Flex,
	IconButton,
	useEditableControls,
} from '@chakra-ui/react'
import { useState } from 'react'
import { ChatMessage } from 'types/chat'

interface ChatMessageContentProps {
	message: ChatMessage
	onSubmit?: (text: string) => void
}
const ChatMessageContent = ({
	message,
	onSubmit: _onSubmit,
}: ChatMessageContentProps) => {
	const [text, setText] = useState(message.message)
	function EditableControls() {
		const {
			isEditing,
			getSubmitButtonProps,
			getCancelButtonProps,
			getEditButtonProps,
		} = useEditableControls()

		return isEditing ? (
			<ButtonGroup justifyContent="left" size="sm">
				<IconButton icon={<CheckIcon />} {...getSubmitButtonProps()} />
				<IconButton icon={<CloseIcon />} {...getCancelButtonProps()} />
			</ButtonGroup>
		) : (
			<Flex justifyContent="left">
				<IconButton size="sm" icon={<EditIcon />} {...getEditButtonProps()} />
			</Flex>
		)
	}

	/**
	 * onCancel reset the text
	 */
	const onCancel = () => {
		setText(message.message)
	}

    /**
	 * onSubmit
	 */
	const onSubmit = () => {
		if (_onSubmit) {
			_onSubmit(text)
		}
	}

    /**
	 * handleOnChange
	 */
	const handleOnChange = (val: string) => {
		setText(val)
	}

	return (
		<Editable
			value={text}
			fontSize="2xl"
			isPreviewFocusable={false}
			onChange={handleOnChange}
			onSubmit={onSubmit}
			onCancel={onCancel}
		>
			<EditablePreview />
			<EditableInput />
			<EditableControls />
		</Editable>
	)
}

export default ChatMessageContent
